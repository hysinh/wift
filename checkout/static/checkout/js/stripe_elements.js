/*
    Core logic/payment flow for this comes from here:
    https://docs.stripe.com/payments/accept-a-payment

    CSS from here:
    https://docs.stripe.com/payments/elements
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
    base: {
        color: '#32325d',
        fontFamily: '"Helvetica", san-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545',
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
            `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                purchase_details: {
                    purchase_number: $.trim(purchase_form.purchase_number.value),
                    member: $.trim(purchase_form.member.value)
                    membership_purchased: $.trim(purchase_form.membership_purchased.value),
                    purchase_date: $.trim(purchase_form.purchase_date.value),
                    purchase_total: $.trim(purchase_form.purchase_total.value),
                }
            },
            member_details: {
                member: $.trim(membership_form.member.value),
                membership_level: $.trim(membership_form.membership_level.value)
                firstname: $.trim(form.default_firstname.value),
                lastname: $.trim(form.default_lastname.value),
                address: {
                    line1: $.trim(form.default_street_address1.value),
                    line2: $.trim(form.default_street_address2.value),
                    city: $.trim(form.default_town_or_city.value),
                    country: $.trim(form.default_country.value),
                    postal_code: $.trim(form.default_postcode.value),
                    state: $.trim(form.default_county.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        // just reload the page, the error will be in djgano messages
        location.reload();
    })
});
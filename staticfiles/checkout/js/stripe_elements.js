/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
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
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            // purchase_details: {
            //     purchase_number: $.trim(purchase_form.purchase_number.value),
            //     member: $.trim(purchase_form.member.value),
            //     membership_purchased: $.trim(purchase_form.membership_purchased.value),
            //     purchase_date: $.trim(purchase_form.purchase_date.value),
            //     purchase_total: $.trim(purchase_form.purchase_total.value),
            // }
        // },
        // member_details: {
        //     member: $.trim(member_data_form.member.value),
        //     membership_level: $.trim(member_data_form.membership_level.value),
        //     default_firstname: $.trim(member_data_form.default_firstname.value),
        //     default_lastname: $.trim(member_data_form.default_lastname.value),
        //     default_street_address1: $.trim(member_data_form.default_street_address1.value),
        //     default_street_address2: $.trim(member_data_form.default_street_address2.value),
        //     default_town_or_city: $.trim(member_data_form.default_town_or_city.value),
        //     default_county: $.trim(member_data_form.default_county.value),
        //     default_postcode: $.trim(member_data_form.default_postcode.value),
        //     default_country: $.trim(member_data_form.default_country.value),
        // },
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>
            `;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);   
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }  
        }
    });
});
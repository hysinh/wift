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

    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
    }
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(() => {
        console.log("After the postData");
        console.log(form);
        var default_firstname = document.getElementById("id_default_firstname").value;
        var default_lastname = document.getElementById("id_default_lastname").value;
        // var name = default_firstname + default_lastname;
        var name = default_firstname.concat(" ", default_lastname);
        console.log(name);
        var member_data_private = {
            name: name,
            address:{
                line1: document.getElementById("id_default_street_address1").value,
                line2: document.getElementById("id_default_street_address2").value,
                city: document.getElementById("id_default_town_or_city").value,
                country: document.getElementById("id_default_country").value,
                state: document.getElementById("id_default_county").value,
                postcode: document.getElementById("id_default_postcode").value,
            }
            // lastname: document.getElementById("id_default_lastname").value,
        }
        console.log(member_data_private);
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {...member_data_private}
                // membership_purchase: {
                //     purchase_details: {
                //         // purchase_number: $.trim(form.purchase_number.value),
                //         // member: $.trim(purchase_form.member.value),
                //         // membership_purchased: $.trim(purchase_form.membership_purchased.value),
                //         // purchase_date: $.trim(purchase_form.purchase_date.value),
                //         // purchase_total: $.trim(purchase_form.purchase_total.value),
                //     }
                // }
            },
            shipping: {...member_data_private},
            // metadata: {...member_data_private},
            // member_data_private: {
            //     // name: $.trim(form.full_name.value),
            //     // member: $.trim(form.member.value),
            //     // membership_level: $.trim(member_data_form.membership_level.value),
            //     // default_firstname: $.trim(form.querySelector("#id_default_firstname").value),
            //     // default_lastname: $.trim(member_data_form.default_lastname.value),
            //     // default_street_address1: $.trim(member_data_form.default_street_address1.value),
            //     // default_street_address2: $.trim(member_data_form.default_street_address2.value),
            //     // default_town_or_city: $.trim(member_data_form.default_town_or_city.value),
            //     // default_county: $.trim(member_data_form.default_county.value),
            //     // default_postcode: $.trim(member_data_form.default_postcode.value),
            //     // default_country: $.trim(member_data_form.default_country.value),
            // },
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
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
    })  
});
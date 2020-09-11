//اگر از این روش استفاده میکنی
//این طور عمل میکند که تو داری انگار یک فرم رو سابمیت میکنی
//هیچ چیزی رو توی روت مسیر نباید بدی
//هر چیزی رو که خواستی بفرستی با کلید دیتا بفرست و توی
//Url
//هم نمیخواد چیزی رو مشخص کنی
//اما باید طوری عمل کنی که انگار داری فرم رو سابمیت میکنی و آخر رویداد سابمیت یک
//return false
//بذار تا صفحه رفرش نشود
// var postBtn = $('#postBtn');
// postBtn.click(function () {
//     var csrf = $("input[name='csrfmiddlewaretoken']").val();
//     alert(csrf);
//     $('#formPost').submit(function (event) {
//         event.preventDefault();
//         //
//         $.ajax({
//             type: 'POST',
//             url: '/test/postData',
//             data: {'csrfmiddlewaretoken': csrf, 'name': 'smaslkamslka'}
//         }).done(function () {
//             alert('sldkjd');
//         });
//         //
//         return false;
//     });
// });


//توی این روش باید توی مسبر هات هم مشخص کنی که چه پارامتری قراره بیاد
//توی اینجا هم باید ادامه ی مسیر رو مشخص کنی با پارامتر عات
// var postBtn = $('#postBtn');
// postBtn.click(function () {
//     var csrf = $("input[name='csrfmiddlewaretoken']").val();
//         //
//         $.ajax({
//             type: 'POST',
//             url: '/test/postData/'+$('#nameSender').val(),
//             data: {'csrfmiddlewaretoken': csrf}
//         }).done(function () {
//             alert('sldkjd');
//         });
// });

$('#sendBtn').click(function () {
    // ValidatorErrorShow();
    var result = validationInputs(collectElements());

    if (result == true){
        sendMessage();
    }

});

function sendMessage() {
    var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
     //alert(csrf_token);
    $.ajax({
        type: "POST",
        url: "/saveMessage",
        data: {
            'csrfmiddlewaretoken': csrf_token,
            'name': $('#name').val(),
            'email': $('#email').val(),
            'phone': $('#phone').val(),
            'message': $('#message').val()
        }
    }).done(function (response) {
        $('#modalTitle').text('وضعیت درخواست شما:');
        $('#modalHeader').addClass('alert alert-primary')
        if (response['status'] == 200) {
            $('#modalBody').html('<div class="alert alert-success text-right" dir="rtl"><h5>' + response['statusText'] + '</h5></div>');
            $('#modalBody').append('<div class="alert alert-warning"><p class="text-right">' + response['infoText'] + '</p></div>')
        } else {
            $('#modalBody').html('<div class="alert alert-danger text-right" dir="rtl"><p>' + response['statusText'] + '</p></div>');
        }
        $('#WorkSampleModal').modal();
    });
}

function collectElements() {
    var obj = [
        {
            'input': $('#name').val(),
            'span': $('#nameError span')
        },
        {
            'input': $('#email').val(),
            'span': $('#emailError span')
        },
        // {
        //     'input': $('#phone').val(),
        //     'span': $('#phoneError span')
        // },
        {
            'input': $('#message').val(),
            'span': $('#messageError span')
        }
    ];
    return obj;
}

// function ValidatorErrorShow() {
//     var name = $('#name').val();
//     var email = $('#email').val();
//     var phone = $('#phone').val();
//     var message = $('#message').val();
//     var errorMessage = '<span id="error" class="text-danger">این فیلد نباید خالی باشد</span>';
//
//     // alert(name + ' ' + email + ' ' + phone + ' ' + message);
//     if (name == '' || name == undefined) {
//         $('#nameError').html(errorMessage);
//         $('#nameError span').attr('id', 'nameErrorContent');
//     } else {
//         $('#nameErrorContent').css({'display': 'none'});
//     }
//
//     if (email == '' || email == undefined) {
//         $('#emailError').html(errorMessage);
//         $('#emailError span').attr('id', 'emailErrorContent');
//     } else if (isEmail(email) == false) {
//         $('#emailError').html('<span id="emailIsValid" class="text-danger">ایمیل شما معتبر نیست!</span>')
//     } else {
//         $('#emailErrorContent').css({'display': 'none'});
//         $('#emailIsValid').css({'display': 'none'});
//     }
//
//     if (message == '' || message == undefined) {
//         $('#messageError').html(errorMessage);
//         $('#messageError span').attr('id', 'messageErrorContent');
//     } else {
//         $('#messageErrorContent').css({'display': 'none'});
//     }
//
//     ValidatorSendMessage();
// }

function isEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

// function ValidatorSendMessage() {
//     var name = $('#name').val();
//     var email = $('#email').val();
//     var phone = $('#phone').val();
//     var message = $('#message').val();
//
//     if ((name != '' || name != undefined) && (email != '' || email != undefined) && (message != '' || message != undefined))
//         if (isEmail(email) == true) {
//
//         }
// }

function validationInputs(object_yourInput_SpanError) {
    var isValid = true;
    for (var i = 0; i < object_yourInput_SpanError.length; i++) {
        if (object_yourInput_SpanError[i]['input'] === '') {
            $(object_yourInput_SpanError[i]['span']).css({'display': 'block'});
            $(object_yourInput_SpanError[i]['span']).html('این فیلد نباید خالی باشد.');
            isValid = false;
        } else {
            if (object_yourInput_SpanError[i]['span'].parent().attr('id') === 'emailError') {
                var result = isEmail(object_yourInput_SpanError[i]['input']);
                if (result === false) {
                    $(object_yourInput_SpanError[i]['span'].css({'display': 'block'}));
                    $(object_yourInput_SpanError[i]['span'].html('ایمیل شما معتبر نیست.'))
                    isValid = false;
                    continue;
                }
            }
            $(object_yourInput_SpanError[i]['span']).css({'display': 'none'});
        }
    }

    return isValid;
}


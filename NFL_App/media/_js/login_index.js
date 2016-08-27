$(function () {
    var user = {},
        flg = {};
    init();
    $('.upload').click(function () {
        if (flg.upd == 0) {
            upd('upload');
            flg.upd = 1
        } else {
            upd('');
            flg.upd = 0
        }
    });
    $('#login').click(function () {
        initub();
        $('#logmsk').fadeIn();
        ub(0)
    });
    $('#logint').click(function () {
        initub();
        if (flg.logt == 0) {
            ub(1);
            flg.logt = 1
        } else {
            ub(0);
            flg.logt = 0
        }
    });
    //Remove this
    $("#name").keyup(function () {
        var len = $('#name').val().length;
        if (len > 13 || len == 0) {
            $('#name').css('background', 'rgb(255, 214, 190)');
            blsp();
            if (len != 0) {
                $('#nameal').css('color', 'rgb(255, 57, 19)').text('ID: Too long').fadeIn()
            } else {
                $('#nameal').css('color', 'rgb(255, 57, 19)').text('ID: Null').fadeIn()
            }
            flg.name = 1
        } else {
            $('#name').css('background', 'rgb(255, 255, 255)');
            $('#nameal').css('color', 'rgb(17, 170, 42)').text('ID: Ok').fadeIn();
            flg.name = 0;
            tcheck()
        }
    });
    //Remove this
    $("#passw").keyup(function () {
        var len = $('#passw').val().length;
        if (len > 10 || len == 0) {
            $('#passw').css('background', 'rgb(255, 214, 190)');
            blsp();
            if (len != 0) {
                $('#passwal').css('color', 'rgb(255, 57, 19)').text('passwword: Too long').fadeIn()
            } else {
                $('#passwal').css('color', 'rgb(255, 57, 19)').text('passwword: Null').fadeIn()
            }
            flg.passw = 1
        } else {
            $('#passw').css('background', 'rgb(255, 255, 255)');
            $('#passwal').css('color', 'rgb(17, 170, 42)').text('passwword: Ok').fadeIn();
            flg.passw = 0;
            tcheck()
        }
    });

    function tcheck() {
        if (flg.name == 0 && flg.passw == 0) {
            $('#signupb').css('opacity', '1').css('cursor', 'pointer')
        } else {
            blsp()
        }
    }
    $('#signupb').click(function () {
        if (flg.name == 0 && flg.passw == 0) {
            $('#sumsk').fadeIn();
            $('#name, #passw, #logint, #nameal, #passwal, #signupb').css('opacity', '0.2');
            $('#close').fadeIn()
        }
    });
    $('#close').click(function () {
        init();
        initub();
        $('#close').hide()
    });

    function init() {
        flg.logt = 0
    }

    function initub() {
        flg.name = -1;
        flg.passw = -1;
        $('#sumsk').hide();
        $('#nameal').hide();
        $('#passwal').hide();
        $('#name, #passw, #logint, #nameal, #passwal, #signupb').css('opacity', '1');
        $('#name').css('background', 'rgb(255, 255, 255)');
        $('#passw').css('background', 'rgb(255, 255, 255)');
        $('#signupb').css('opacity', '0.2').css('cursor', 'default');
        $('#name, #passw').val('')
    }

    function upd(button) {
        location.hash = button;
        if (flg.upd == 0) {
            $('#drop').fadeIn()
        } else {
            $('#drop').fadeOut()
        }
    }

    function blsp() {
        $('#signupb').css('opacity', '0.2').css('cursor', 'default')
    }
});
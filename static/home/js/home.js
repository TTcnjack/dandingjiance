$(function () {
    $("#rt_run_rate").click(function () {
        $(window).attr('location',"running_rate/");
        // location.href = {% url 'danding:running_rate'%};
    })

});
$(function () {
    $("#output").click(function () {
        $(window).attr('location',"output/");
        // location.href = {% url 'danding:output'%};
    })

});
$(function () {
    $("#break_per").click(function () {
        $(window).attr('location',"break_per/");
        // location.href = {% url 'danding:break_per'%};
    })

});
$(function () {
    $("#weak_twist").click(function () {
        $(window).attr('location',"weak_twist/");
        // location.href = {% url 'danding:weak_twist'%};
    })

});
$(function () {
    $("#empty_ingot").click(function () {
        $(window).attr('location',"empty_ingot/");
        // location.href = {% url 'danding:empty_ingot'%};
    })

});
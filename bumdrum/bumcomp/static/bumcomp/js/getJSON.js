var pbp = {};

function getpbp(away, home, date, f) {
    $.getJSON("/bumcomp/json/pbp/DET/CHC/20180704", f) ;
}

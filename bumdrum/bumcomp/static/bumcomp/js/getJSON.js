var pbp = {};

function getpbp(away, home, date, f) {
    var url = `/bumcomp/json/pbp/${away}/${home}/${date}`
    $.getJSON( url, f) ;
}

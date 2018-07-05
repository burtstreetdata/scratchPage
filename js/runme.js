var RUNME = {};
RUNME.dset = [3, 5, 7, 11, 23] ;
RUNME.fubcount= 0;
RUNME.fubs=[];
RUNME.fubwidth = 22 ;
RUNME.fubpad = 2;
RUNME.svgheight = 200;


var svg =    d3.select("body").append("svg")
    .attr("class","fub")
    .attr("width", (RUNME.fubwidth + RUNME.fubpad) * RUNME.dset.length)
    .attr("height", RUNME.svgheight );

RUNME.fx = function (d){
    return  d
}

svg.selectAll("rect")
    .data(RUNME.dset)
    .enter()
    .append("rect")
    .attr("x", function(d,i){
	return i * (RUNME.fubwidth + RUNME.fubpad)
    })
    .attr("y",   function(d) {
	return RUNME.svgheight - d *  10 ;
    })
    .attr("width", RUNME.fubwidth)
    .attr("height",  function(d) {
	return d * 10;
    })
    .attr("fill", function(d) {
	return "rgb(0, "  + Math.round(50+d*20) + ", 0)";
    })
;

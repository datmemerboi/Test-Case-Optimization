var can = document.getElementById('result-graph');

var chart = new Chart( can, {
	type: 'bar',
	data: {
		labels : xaxis,
		datasets: [{
			label : "GA iterations",
			data : yaxis,
			backgroundColor: ga_colorArray,
			borderColor: ga_borderArray,
			borderWidth: 1.5
		}]
	}
});
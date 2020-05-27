var can = document.getElementById('result-graph');

var chart = new Chart( can, {
	type: 'bar',
	data: {
		labels : xaxis,
		datasets: [{
			label : "PSO iterations",
			data : yaxis,
			backgroundColor: pso_colorArray,
			borderColor: pso_borderArray,
			borderWidth: 1.5
		}]
	}
});
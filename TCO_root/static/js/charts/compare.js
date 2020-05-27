var can = document.getElementById('result-graph');

var chart = new Chart( can, {
	type: 'bar',
	data: {
		labels : pso_xaxis,
		datasets: [
		{
			label: "PSO iterations",
			data: pso_yaxis,
			backgroundColor: pso_colorArray,
			borderColor: pso_borderArray,
			borderWidth: 1.5
		},
		{
			label : "GA iterations",
			data : ga_yaxis,
			backgroundColor: ga_colorArray,
			borderColor: ga_borderArray,
			borderWidth: 1.5
		}],
	},
	options: {
		scales:{
			xAxes:[{
				stacked: true,
				scaleLabel:{display:true,labelString: "Iterations"}
			}],
			yAxes:[{
				stacked: false,
				scaleLabel:{display:true,labelString: "seconds"}
			}]
		}
	}
});

var can = document.getElementById('time');
var chart = new Chart( can, {
	type:'doughnut',
	data: {
		labels:['PSO', 'GA'],
		datasets:[{
			data: [pso_time, ga_time],
			backgroundColor: [primaryColor, secondaryColor],
			borderColor: [primaryBorder, secondaryBorder],
			borderWidth: 2
		}]
	},
});
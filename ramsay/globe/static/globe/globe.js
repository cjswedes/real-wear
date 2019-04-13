
 class Point extends React.Component	{
	constructor(props) {
		super(props);
	}

	render() {
		let point_proj = d3.geoOrthographic()

		let point_generator = d3.geoPath().projection(projection)

		let circle = d3.geoCircle().center([this.props.cx, this.props.cy]).radius(2)
		let pathString = point_generator(circle())
		return React.createElement("path", {d : pathString});
	}
}


class Globe extends React.Component {
	constructor(props) {
		super(props);

		this.state = {
			rotation: 0 };

	}

	render() {
		let projection = d3.geoOrthographic().
		fitSize([this.props.size, this.props.size], this.props.geoJson).
		rotate([this.state.rotation]);

		let geoGenerator = d3.geoPath().
		projection(projection);

		
		let pathString = geoGenerator(this.props.geoJson);

		window.requestAnimationFrame(() => {
			this.setState({
				rotation: this.state.rotation + 0.2 });

		});

		return React.createElement("svg", { width: this.props.size, height: this.props.size },
    React.createElement("circle", { cx: this.props.size / 2, cy: this.props.size / 2, r: this.props.size / 2, fill: "#b7d3ff" }),
    React.createElement("path", { d: pathString, id:"countries" }), 
    pcoords.map(
    	function(pair, index) {
    		//let point_proj = d3.geoOrthographic()

			//let point_generator = d3.geoPath().projection(point_proj)

			let circle = d3.geoCircle().center([pair[0], pair[1]]).radius(0.5)
			let circleString = geoGenerator(circle())
			return React.createElement("path", {d : circleString, key: index, id : "points"});
    	} ));
	}
}
//React.createElement("path", {d : geoGenerator(d3.geoCircle().center(pair).radius(2)()), key : index}))

//console.log(JSON.parse(document.getElementById('plong').textContent));
//console.log(pjson)
//console.log(typeof pjson)

var pcoords = []
var mcoords = []
for(pair in pjson) {
	//console.log(pjson[pair])
	var new_pair = []
	for(string in pjson[pair]) {
		new_pair.push(parseFloat(pjson[pair][string]))
	}
	
	if(new_pair[0] !== 0 && new_pair[1] !== 0) {
		//console.log(new_pair)
		pcoords.push(new_pair)
	}
}
for(pair in mjson) {
	var new_pair = []
	for(string in mjson[pair]) {
		new_pair.push(parseFloat(pjson[pair][string]))	
	}
	if(new_pair !== [0, 0]) {
		mcoords.push(new_pair)
	}
}
//console.log(pcoords)


d3.json(globeJson).then((json) => {
	let geoJson = topojson.feature(json, json.objects.ne_110m_admin_0_countries);

	ReactDOM.render(
		React.createElement(Globe, { geoJson: geoJson, size: 400 }),
		document.getElementById('app'));

});
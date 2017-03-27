module.exports = {
    entry: './source/index.js',
    output: {
	filename: 'index.js',
	path: './static/js'
    },
    module: {
	loaders: [
	    {
		test: /\.jsx?$/,
		exclude: /node_modules/,
		loader: 'babel-loader',
		query:{
		    presets: ['es2016', 'react']
		}
	    }
	]
    },
    target: 'web'
};

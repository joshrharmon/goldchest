const path = require('path');
const webpack = require('webpack');
const HtmlWebPackPlugin = require("html-webpack-plugin");



module.exports = {
    entry: './src/components/App.js',
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, 'static/frontend'),
    },
    module: {
        rules: [

            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },

        ]
    },
    plugins: [
        // Added as a plugin so that imports in js work
        new webpack.ProvidePlugin({
            "React": "react"
        })

    ]
};




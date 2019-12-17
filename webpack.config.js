const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  entry: ['./static/src/index.js', './static/src/index.scss'],
  output: {
    filename: 'index.js',
    path: path.resolve(__dirname, 'static/dist'),
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "index.css"
    })
  ],
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
            MiniCssExtractPlugin.loader,
            'css-loader',
            'sass-loader'
        ]
      },
    ]
  },
};
const autoprefixer = require('autoprefixer');
const path = require('path');


module.exports = {
  resolve: {
        extensions: ['.js', '.jsx']
    },
  module: {
    rules: [
        {
            test: /\.js$/,
            loader: 'babel-loader',
            exclude: /node_modules/
        },
        {
            test: /\.css$/,
            exclude: /node_modules/,
            use: [
                { loader: 'style-loader' },
                {
                    loader: 'css-loader',
                    options: {
                        modules: {
                            localIdentName: "[name]__[local]___[hash:base64:5]",
                        },
                        sourceMap: true
                    }
                 },
                 {
                     loader: 'postcss-loader',
                     options: {
                         ident: 'postcss',
                         plugins: () => [
                             autoprefixer({})
                         ]
                     }
                  }
            ]
        },
        {
            test: /\.(jpg|png|jpeg|gif)$/,
            loader: 'url-loader?limit=10000&name=static/frontend/[name].[ext]'
        },
        {
            test: /\.html$/,
            use: [
              {
                loader: "html-loader"
              }
            ]
          },
          {
            test: /\.svg$/,
            use: ['@svgr/webpack', 'url-loader'],
          },
    ]
},

};

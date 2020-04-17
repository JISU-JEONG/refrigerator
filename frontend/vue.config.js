module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
    disableHostCheck: true,
    proxy: {
      "/openapi/": {
        target: "http://211.237.50.150:7080/openapi/",
        changeOrigin: true,
        pathRewrite: {
          "^/openapi": ""
        }
      },
      "/recipes/": {
        target: "http://211.213.225.87:8085/recipes/",
        changeOrigin: true,
        pathRewrite: {
          "^/recipes": ""
        }
      }
    }
  }
};

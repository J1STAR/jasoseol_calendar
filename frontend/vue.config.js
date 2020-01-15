'use strict';

module.exports = {
    devServer: {
        proxy: {
            "/api": {
                target: "http://j1star.ddns.net:8000",
                changeOrigin: true
            },
        },
        disableHostCheck: true,
    }
};

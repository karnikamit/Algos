var app = angular.module('myApp', []);
    app.controller('myCtrl', function($scope){
        var appCtrl = this;
        appCtrl.searchParam = '';
        appCtrl.records = {
            amit: {
                name: "amit",
                age: '27'
            }
        };
        appCtrl.search = function(value){
            return appCtrl.records.value
        };
    });

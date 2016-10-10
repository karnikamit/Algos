var app = angular.module('myApp', []);
    app.controller('myCtrl', function($scope){
        var appCtrl = this;
        appCtrl.searchParam = '';
        $scope.records = {
            amit: {
                name: "amit",
                age: '27',
                sex: 'Male',
                relationship: 'Single'
            }
        };
        appCtrl.search = function(value){
            return $scope.records.value
        };
    });

    app.directive('myDirective', function(){
        var myDirc = this;
        myDirc
    });

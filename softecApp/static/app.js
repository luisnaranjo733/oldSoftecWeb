'use strict';

var softecApp = angular.module('softecApp', []);
softecApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});

softecApp.controller('softecCtrl', function($scope) {

    $scope.adjective =  'salty';
    $scope.firstNoun = 'chair';
    $scope.secondNoun = 'fido';
});
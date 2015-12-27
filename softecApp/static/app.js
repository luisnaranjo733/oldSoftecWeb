'use strict';

var softecApp = angular.module('softecApp', []);

softecApp.controller('softecCtrl', function($scope) {

    $scope.adjective =  'salty';
    $scope.firstNoun = 'chair';
    $scope.secondNoun = 'fido';
});
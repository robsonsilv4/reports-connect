'use strict';

angular
  .module('app', [], function ($locationProvider, $interpolateProvider) {
    $locationProvider.html5Mode(true);
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  })
  .run(function ($rootScope) {
    $rootScope.baseUrl = 'http://127.0.0.1:8000';
  });

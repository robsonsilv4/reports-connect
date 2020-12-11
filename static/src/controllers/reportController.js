(function () {
  'use strict';
  angular
    .module('app')
    .controller('ReportController', function ($scope, $rootScope, $http) {
      $http.get(`${$rootScope.baseUrl}/reports/`).then(function (response) {
        const reports = response.data.results;
        $scope.reports = reports;
      });
    });
})();

(function () {
  'use strict';
  angular
    .module('app')
    .controller('ReportController', function ($scope, $rootScope, $http) {
      $scope.showModal = false;

      $scope.toggleModal = function () {
        console.log($scope.showModal);
        $scope.showModal = !$scope.showModal;
      };

      $http.get(`${$rootScope.baseUrl}/reports/`).then(function (response) {
        const reports = response.data.results;
        $scope.reports = reports;
      });
    });
})();

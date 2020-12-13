(function () {
  'use strict';

  angular
    .module('app')
    .controller(
      'UsersController',
      function ($scope, $rootScope, $http, UserService) {
        var url = $rootScope.baseUrl + '/users/';

        $http.get(url).then(function (response) {
          var users = response.data.results;
          $scope.users = users;
        });

        $scope.selectUser = function (selectedUser) {
          $scope.selectedUser = selectedUser;
          UserService.setCurrentUser(selectedUser);
        };
      }
    );
})();

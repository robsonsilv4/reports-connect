(function () {
  'use strict';

  angular.module('app').factory('UserService', function () {
    var user = {};

    function getUser() {
      var currentUser = localStorage.getItem('currentUser');

      if (currentUser) {
        user = currentUser;
      }

      return user;
    }

    function setUser(newUser) {
      user = newUser;
      localStorage.setItem('currentUser', user);
    }

    return {
      getUser: getUser,
      setUser: setUser,
    };
  });
})();

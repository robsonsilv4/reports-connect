(function () {
  'use strict';

  angular.module('app').factory('UserService', function () {
    var user = '';

    function getUser() {
      return user;
    }

    function setUser(newUser) {
      user = newUser;
    }

    function clear() {
      user = '';
    }

    return {
      getUser: getUser,
      setUser: setUser,
      clear: clear,
    };
  });
})();

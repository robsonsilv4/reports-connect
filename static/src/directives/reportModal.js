(function () {
  'use strict';

  angular.module('app').directive('reportModal', function () {
    return {
      restrict: 'E',
      scope: {
        show: '=',
      },
      replace: true,
      transclude: true,
      link: function (scope, _element, _attrs) {
        scope.hideModal = function () {
          scope.show = false;
        };
      },
      template: `
        <div class="modal is-active" ng-show="show">
          <div class="modal-background"></div>
          <div class="modal-card">
            <header class="modal-card-head">
              <p class="modal-card-title">Responses</p>
              <button class="delete" ng-click="hideModal()"></button>
            </header>
            <section class="modal-card-body" ng-transclude></section>
          </div>
        </div>
        `,
    };
  });
})();

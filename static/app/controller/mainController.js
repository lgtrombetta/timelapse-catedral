app.controller('mainController', ["$scope", "$http", function ($scope, $http) {
        $scope.p=1;
        $http.get("/capture/").then(function (data) {
              $scope.datos = data;
          });

}]);

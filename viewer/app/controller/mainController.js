app.controller('mainController', ["$scope", "$http", function ($scope, $http) {
    function init() {
        $http({
            url: "capture",
            method: "POST",
            data: { },
        }).success(function (data) {
            $scope.data = data;
        });
    }

    init();

}]);

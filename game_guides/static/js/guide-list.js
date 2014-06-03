app = angular.module('guides.list', []);

app.controller('GuideListController', [
    '$scope', '$http', function($scope, $http) {
        $scope.filters = { };
        $scope.guides = [];
        return $http.get('/api/guides').then(function(result) {
            return angular.forEach(result.data, function(item) {
                return $scope.guides.push(item);
            });
        });
    }
]);

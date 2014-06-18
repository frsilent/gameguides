var app = angular.module('guides.list', [])

app.controller('GuideListController', ['$scope', '$http', '$filter', function($scope, $http, $filter) {
    $scope.guides = [];
    $scope.categories = [];
    $http.get('/api/guides').then(function(result) {
        // Fetches all guides from /api/guides endpoint
        angular.forEach(result.data, function(item) {
            $scope.guides.push(item);
        });
    });

    // Pagination uses the app 'paginate' function
    $scope.currentPage = 0;
    $scope.pageSize = 6;

    $scope.toggleCategory = function(category_id) {
        // Adds or removes a category id from $scope.categories
        var exists = $filter('filter')($scope.categories, category_id, true);
        if(exists.length) {
            $scope.categories.pop(category_id);
        } else {
            $scope.categories.push(category_id);
        };
        $scope.currentPage = 0;
    };

    $scope.category_filter = function(guide) {
        // filters out guides that do not have any categories in the current $scope.categories
        if(!$scope.categories.length) { return true; }
        for(var i = 0, len = $scope.categories.length; i < len; i++) {
            if(guide.categories.indexOf($scope.categories[i]) == -1) {
                return false;
            }
        }
        return true;
    };

}]);

app.filter('paginate', function() {
    return function(input, start) {
        start = +start; //parse to int
        return input.slice(start);
    }
});

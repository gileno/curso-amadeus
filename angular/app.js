var app = angular.module("CoursesApp", []);

app.controller("CourseListController", function($scope, $http) {
    $http.get('http://localhost:8080/api/cursos/').
        success(function(data, status, headers, config) {
          $scope.courses = data;
    });
});

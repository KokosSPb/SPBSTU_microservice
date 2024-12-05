<?php
header("Content-Type: application/json");
require_once 'config.php';
require_once 'functions.php';

$method = $_SERVER['REQUEST_METHOD'];

switch ($method) {
    case "GET": // получение данных
		$q = $_GET['q'];

		$params = explode('/',$q);
		$type = $params[0];
		if(isset($params[1]))
		{
			$id = $params[1];
			$group = $params[1];
		}

		if($type === 'students')
			if(isset($id))
				getStudent($DBH, $id);
			else
				getStudents($DBH);
			
		if($type === 'groups')
			if(isset($id))
				getGroup($DBH, $id);
			else
				getGroups($DBH);
		if($type === 'list')
			if(isset($id))
				listStudentsGroupId($DBH, $id);
		break;
	case "POST": // добавление данных
		if($_GET['q'] === 'students')
			addStudent($DBH, $_POST);
		if($_GET['q'] === 'groups')
			addGroup($DBH, $_POST);
		if($_GET['q'] === 'list')
			listStudentsGroup($DBH, $_POST);
		break;
	case "PATCH": // внесение изменений
		$q = $_GET['q'];
		
		$params = explode('/',$q);
		$type = $params[0];
		if(isset($params[1]))
			$id = $params[1];
		if($type === 'students')
			if(isset($id))
			{
				$data = file_get_contents('php://input');
				$data = json_decode($data, true);
				chGroup($DBH, $id, $data);
			}
		break;
	case "DELETE": // внесение изменений
		$q = $_GET['q'];
		
		$params = explode('/',$q);
		$type = $params[0];
		if(isset($params[1]))
		{
			$id = $params[1];
			if($type === 'students')
				delStudent($DBH, $id);
			if($type === 'groups')
				delGroup($DBH, $id);
		}
		break;
	default:
		break;
}
?>
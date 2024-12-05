<?php
function addStudent($DBH, $data)
{
	$STH = $DBH->prepare("INSERT INTO `students` (`id`, `name`, `fname`, `lname`, `gr`) VALUES (NULL, '".$data['name']."', '".$data['fname']."', '".$data['lname']."', '".$data['gr']."');");
	$STH->execute();
	http_response_code(201);
	$ar = [
			"status" => true,
			"id" => $DBH->lastInsertId()
		];
	echo json_encode($ar);
}
function getStudents($DBH)
{
	$STH = $DBH->prepare("Select * from `students`");
	$STH->setFetchMode(PDO::FETCH_ASSOC);
	$STH->execute();
	if($STH->rowCount()) // Если база не пустая
	{
		while($r = $STH->fetch())
			$ar[] = $r;
	}
	else
	{
		http_response_code(404);
		$ar = [
			"status" => false,
			"message" => "students not found"
		]; // База пустая
	}
	echo json_encode($ar);
}
function getStudent($DBH, $id)
{
	$STH = $DBH->prepare("Select * from `students` where `id` = '".$id."'");
	$STH->setFetchMode(PDO::FETCH_ASSOC);
	$STH->execute();
	if($STH->rowCount()) // Если база не пустая
	{
		$r = $STH->fetch();
		$ar[] = $r;
	}
	else
	{
		http_response_code(404);
		$ar = [
			"status" => false,
			"message" => "student not found"
		]; // База пустая
	}
	echo json_encode($ar);
}
function addGroup($DBH, $data)
{
	$STH = $DBH->prepare("INSERT INTO `gr` (`id`, `gr`, `caption`) VALUES (NULL, '".$data['gr']."', '".$data['caption']."');");
	$STH->execute();
	http_response_code(201);
	$ar = [
			"status" => true,
			"id" => $DBH->lastInsertId()
		];
	echo json_encode($ar);
}
function getGroups($DBH)
{
	$STH = $DBH->prepare("Select * from `gr`");
	$STH->setFetchMode(PDO::FETCH_ASSOC);
	$STH->execute();
	if($STH->rowCount()) // Если база не пустая
	{
		while($r = $STH->fetch())
			$ar[] = $r;
	}
	else
	{
		http_response_code(404);
		$ar = [
			"status" => false,
			"message" => "Groups not found"
		]; // База пустая
	}
	echo json_encode($ar);
}
function getGroup($DBH, $id)
{
	$STH = $DBH->prepare("Select * from `gr` where `id` = '".$id."'");
	$STH->setFetchMode(PDO::FETCH_ASSOC);
	$STH->execute();
	if($STH->rowCount()) // Если база не пустая
	{
		$r = $STH->fetch();
		$ar[] = $r;
	}
	else
	{
		http_response_code(404);
		$ar = [
			"status" => false,
			"message" => "Group not found"
		]; // База пустая
	}
	echo json_encode($ar);
}
function chGroup($DBH, $id, $data)
{
	$STH = $DBH->prepare("Select * from `students` where `id` = '".$id."'");
	$STH->setFetchMode(PDO::FETCH_ASSOC);
	$STH->execute();
	if($STH->rowCount()) // Если такой студент существует
	{
		$STH = $DBH->prepare("UPDATE `students` SET `gr` = '".$data['gr_new']."' WHERE `students`.`id` = '".$id."'");
		$STH->execute();
		http_response_code(200);
		$ar = [
				"status" => true,
				"message" => "Group is update"
			];
	}
	else
	{
		http_response_code(404);
		$ar = [
			"status" => false,
			"message" => "student not found"
		]; // База пустая
	}
	echo json_encode($ar);

}
function delStudent($DBH, $id)
{
	$STH = $DBH->prepare("Select * from `students` where `id` = '".$id."'");
	$STH->setFetchMode(PDO::FETCH_ASSOC);
	$STH->execute();
	if($STH->rowCount()) // Если такой студент существует
	{
		$STH = $DBH->prepare("DELETE FROM `students` WHERE `students`.`id` = '".$id."'");
		$STH->execute();
		http_response_code(200);
		$ar = [
				"status" => true,
				"message" => "Delete student successful"
			];
	}
	else
	{
		http_response_code(404);
		$ar = [
			"status" => false,
			"message" => "student not found"
		]; // База пустая
	}
	echo json_encode($ar);
}
function delGroup($DBH, $id)
{
	$STH = $DBH->prepare("Select * from `gr` where `id` = '".$id."'");
	$STH->setFetchMode(PDO::FETCH_ASSOC);
	$STH->execute();
	if($STH->rowCount()) // Если такой студент существует
	{
		$STH = $DBH->prepare("DELETE FROM `gr` WHERE `gr`.`id` = '".$id."'");
		$STH->execute();
		http_response_code(200);
		$ar = [
				"status" => true,
				"message" => "Delete group successful"
			];
	}
	else
	{
		http_response_code(404);
		$ar = [
			"status" => false,
			"message" => "group not found"
		]; // База пустая
	}
	echo json_encode($ar);
}
function listStudentsGroupId($DBH, $id)
{
	$STH = $DBH->prepare("Select `students`.`id`,`students`.`name`,`students`.`fname`,`students`.`lname`,`gr`.`gr` from `students`,`gr` where `gr`.`id` = `students`.`gr` and `gr`.`id` = '".$id."'");
	$STH->setFetchMode(PDO::FETCH_ASSOC);
	$STH->execute();
	if($STH->rowCount()) // Если база не пустая
	{
		while($r = $STH->fetch())
			$ar[] = $r;
	}
	else
	{
		http_response_code(404);
		$ar = [
			"status" => false,
			"message" => "students or group not found"
		]; // База пустая
	}
	echo json_encode($ar);
}
function listStudentsGroup($DBH, $data)
{
	$STH = $DBH->prepare("Select `students`.`id`,`students`.`name`,`students`.`fname`,`students`.`lname` from `students`,`gr` where `gr`.`id` = `students`.`gr` and `gr`.`gr` = '".$data['gr']."'");
	$STH->setFetchMode(PDO::FETCH_ASSOC);
	$STH->execute();
	if($STH->rowCount()) // Если база не пустая
	{
		while($r = $STH->fetch())
			$ar[] = $r;
	}
	else
	{
		http_response_code(404);
		$ar = [
			"status" => false,
			"message" => "students or group not found"
		]; // База пустая
	}
	echo json_encode($ar);
}
?>
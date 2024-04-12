<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $child_names = $_POST['child_name'];

    // Check if any child names are entered
    if (!empty($child_names)) {
        // Process each child name
        foreach ($child_names as $key => $name) {
            // Generate unique ID for each child
            $child_id = uniqid('child_');

            // Save child details or perform any other operations
            echo "Child Name: " . $name . ", Child ID: " . $child_id . "<br>";
        }
    } else {
        echo "No child names entered.";
    }
}
?>

/*jshint esversion: 6 */
/*globals bootstrap */

/* Modal Code Source: Code Institute Django Blog Walk Through Project */
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

console.log("hello");
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let profileId = e.target.getAttribute("data-profile_id");
    deleteConfirm.href = `../delete_profile/${profileId}`;
    deleteModal.show();
  });
}


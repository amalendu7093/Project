 function confirmDelete(employeeId) {
            if (confirm('Are you sure you want to delete this employee? This action cannot be undone.')) {
                document.getElementById('delete-form-' + employeeId).submit();
            }
        }
# Define all tests in a dictionary with flexible coverage exclusion lines
set tests {
    test1-name {
        {file_addr "/path/to/src1"}
        {file_name "file1"}
        {line_numbers {123 125 127}}  # List of lines to exclude
        {description "Test 1 - Checking basic functionality"}
    }
    test2-name {
        {file_addr "/path/to/src2"}
        {file_name "file2"}
        {line_numbers {456}}  # Single line or multiple lines can be specified
        {description "Test 2 - Edge case handling"}
    }
    test3-name {
        {file_addr "/path/to/src3"}
        {file_name "file3"}
        {line_numbers {}}  # No lines to exclude
        {description "Test 3 - Full coverage test"}
    }
}
return $tests

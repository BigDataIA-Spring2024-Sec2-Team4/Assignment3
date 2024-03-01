SELECT
    pdf.Headings AS Main_Heading,
    TRIM(s.value)::VARCHAR AS Sub_Heading_Separated
FROM raw_test.pdf.ptable pdf,
LATERAL FLATTEN(input => SPLIT(pdf.Topics, '|')) s
WHERE s.value IS NOT NULL AND TRIM(s.value) <> ''


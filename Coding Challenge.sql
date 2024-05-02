create database CareerHub;
use CareerHub

-- Create the Companies table
CREATE TABLE Companies (
    CompanyID INT PRIMARY KEY,
    CompanyName VARCHAR(255) NOT NULL,
    Location VARCHAR(255)
);

-- Create the Jobs table
CREATE TABLE Jobs (
    JobID INT PRIMARY KEY,
    CompanyID INT FOREIGN KEY REFERENCES Companies(CompanyID),
    JobTitle VARCHAR(255) NOT NULL,
    JobDescription TEXT,
    JobLocation VARCHAR(255),
    Salary DECIMAL(10, 2),
    JobType VARCHAR(50),
    PostedDate DATETIME
);

-- Create the Applicants table
CREATE TABLE Applicants (
    ApplicantID INT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Phone VARCHAR(20),
	City VARCHAR(100),
    State VARCHAR(100),
    Resume TEXT
);

-- Create the Applications table
CREATE TABLE Applications (
    ApplicationID INT PRIMARY KEY,
    JobID INT FOREIGN KEY REFERENCES Jobs(JobID),
    ApplicantID INT FOREIGN KEY REFERENCES Applicants(ApplicantID),
    ApplicationDate DATETIME NOT NULL,
    CoverLetter TEXT
);
INSERT INTO Companies (CompanyID,CompanyName, Location) VALUES
(1,'Tech Innovations', 'San Francisco'),
(2,'Data Driven Inc', 'New York'),
(3,'GreenTech Solutions', 'Austin'),
(4,'CodeCrafters', 'Boston'),
(5,'HexaWare Technologies', 'Chennai');

INSERT INTO Jobs (JobID,CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate) VALUES
(4001,1, 'Frontend Developer', 'Develop user-facing features', 'San Francisco', 75000, 'Full-time', '2023-01-10'),
(4002,2, 'Data Analyst', 'Interpret data models', 'New York', 68000, 'Full-time', '2023-02-20'),
(4003,3, 'Environmental Engineer', 'Develop environmental solutions', 'Austin', 85000, 'Full-time', '2023-03-15'),
(4004,1, 'Backend Developer', 'Handle server-side logic', 'Remote', 77000, 'Full-time', '2023-04-05'),
(4005,4, 'Software Engineer', 'Develop and test software systems', 'Boston', 90000, 'Full-time', '2023-01-18'),
(4006,5, 'HR Coordinator', 'Manage hiring processes', 'Chennai', 45000, 'Contract', '2023-04-25'),
(4007,2, 'Senior Data Analyst', 'Lead data strategies', 'New York', 95000, 'Full-time', '2023-01-22');

INSERT INTO Applicants (ApplicantID,FirstName, LastName, Email, Phone,City,State, Resume) VALUES
(01,'John', 'Doe', 'john.doe@example.com', '123-456-7890','Chennai','TamilNadu', 'Experienced web developer with 5 years of experience.'),
(02,'Jane', 'Smith', 'jane.smith@example.com', '234-567-8901','tirchy','TamilNadu', 'Data enthusiast with 3 years of experience in data analysis.'),
(03,'Alice', 'Johnson', 'alice.johnson@example.com', '345-678-9012','Karur','TamilNadu', 'Environmental engineer with 4 years of field experience.'),
(04,'Bob', 'Brown', 'bob.brown@example.com', '456-789-0123','Chennai','TamilNadu', 'Seasoned software engineer with 8 years of experience.');

INSERT INTO Applications (ApplicationID,JobID, ApplicantID, ApplicationDate, CoverLetter) VALUES
(1001,4001, 01, '2023-04-01', 'I am excited to apply for the Frontend Developer position.'),
(1002,4002, 02, '2023-04-02', 'I am interested in the Data Analyst position.'),
(1003,4003, 03, '2023-04-03', 'I am eager to bring my expertise to your team as an Environmental Engineer.'),
(1004,4004, 04, '2023-04-04', 'I am applying for the Backend Developer role to leverage my skills.'),
(1005,4005, 01, '2023-04-05', 'I am also interested in the Software Engineer position at CodeCrafters.');

--5.Write an SQL query to count the number of applications received for each job listing in the "Jobs" table. Display the job title and the corresponding application count. Ensure that it lists all jobs, even if they have no applications.
select * from Companies;
select * from Jobs;
SELECT j.JobTitle, COUNT(a.ApplicationID) AS ApplicationCount
FROM Jobs j
LEFT JOIN Applications a ON j.JobID = a.JobID
GROUP BY j.JobTitle;
select * from Applicants;
select*from Applications;

--6. Develop an SQL query that retrieves job listings from the "Jobs" table within a specified salary range. Allow parameters for the minimum and maximum salary values. Display the job title,
DECLARE @MinSalary DECIMAL(10, 2) = 50000.00;
DECLARE @MaxSalary DECIMAL(10, 2) = 100000.00;

SELECT j.JobTitle, c.CompanyName, j.JobLocation, j.Salary
FROM Jobs j
JOIN Companies c ON j.CompanyID = c.CompanyID
WHERE j.Salary BETWEEN @MinSalary AND @MaxSalary;

--7. Write an SQL query that retrieves the job application history for a specific applicant. Allow a parameter for the ApplicantID, and return a result set with the job titles, company names, and application dates for all the jobs the applicant has applied to.
DECLARE @ApplicantID INT = 1;

SELECT j.JobTitle, c.CompanyName, a.ApplicationDate
FROM Applications a
JOIN Jobs j ON a.JobID = j.JobID
JOIN Companies c ON j.CompanyID = c.CompanyID
WHERE a.ApplicantID = @ApplicantID;

--8. Create an SQL query that calculates and displays the average salary offered by all companies for job listings in the "Jobs" table. Ensure that the query filters out jobs with a salary of zero.
SELECT AVG(Salary) AS AverageSalary
FROM Jobs
WHERE Salary > 0;

--9. Write an SQL query to identify the company that has posted the most job listings. Display the company name along with the count of job listings they have posted. Handle ties if multiple companies have the same maximum count.
SELECT TOP 1 WITH TIES c.CompanyName, COUNT(j.JobID) AS JobListingCount
FROM Companies c
JOIN Jobs j ON c.CompanyID = j.CompanyID
GROUP BY c.CompanyName
ORDER BY COUNT(j.JobID) DESC;


--10. Find the applicants who have applied for positions in companies located in 'CityX' and have at least 3 years of experience.
declare @c varchar(50)='boston';
select concat(firstname,' ',lastname) as Name
from Applicants 
where ApplicantID in(select ApplicantID
					from jobs j inner join Applications a
					on j.JobID=a.JobID
					where JobLocation=@c)
and (Resume like '%3%' or 
Resume like '%4%' or
Resume like '%5%' or 
Resume like '%6%' or 
Resume like '%7%' or
Resume like '%8%' or 
Resume like '%9%' or
Resume like '%10%')

--11. Retrieve a list of distinct job titles with salaries between $60,000 and $80,000.
SELECT DISTINCT JobTitle
FROM Jobs
WHERE Salary BETWEEN 60000 AND 80000;

--12. Find the jobs that have not received any applications.
SELECT j.JobTitle
FROM Jobs j
LEFT JOIN Applications a ON j.JobID = a.JobID
WHERE a.ApplicationID IS NULL;

--13. Retrieve a list of job applicants along with the companies they have applied to and the positions they have applied for.
SELECT a.FirstName, a.LastName, c.CompanyName, j.JobTitle
FROM Applicants a
JOIN Applications ap ON a.ApplicantID = ap.ApplicantID
JOIN Jobs j ON ap.JobID = j.JobID
JOIN Companies c ON j.CompanyID = c.CompanyID;

--14. Retrieve a list of companies along with the count of jobs they have posted, even if they have not received any applications.
SELECT c.CompanyName, COUNT(j.JobID) AS JobCount
FROM Companies c
LEFT JOIN Jobs j ON c.CompanyID = j.CompanyID
GROUP BY c.CompanyName;

--15. List all applicants along with the companies and positions they have applied for, including those who have not applied.
SELECT a.FirstName, a.LastName, c.CompanyName, j.JobTitle
FROM Applicants a
CROSS JOIN Companies c
LEFT JOIN (
    SELECT ap.ApplicantID, j.JobID, j.CompanyID, j.JobTitle
    FROM Applications ap
    JOIN Jobs j ON ap.JobID = j.JobID
) AS ApplicantJobs ON a.ApplicantID = ApplicantJobs.ApplicantID AND c.CompanyID = ApplicantJobs.CompanyID
LEFT JOIN Jobs j ON ApplicantJobs.JobID = j.JobID;

--16. Find companies that have posted jobs with a salary higher than the average salary of all jobs.
SELECT c.CompanyName
FROM Companies c
JOIN Jobs j ON c.CompanyID = j.CompanyID
WHERE j.Salary > (
    SELECT AVG(Salary)
    FROM Jobs
    WHERE Salary > 0
);

--17. Display a list of applicants with their names and a concatenated string of their city and state
SELECT FirstName, LastName, CONCAT(City, ', ', State) AS Location
FROM Applicants;

--18. Retrieve a list of jobs with titles containing either 'Developer' or 'Engineer'.
SELECT JobTitle
FROM Jobs
WHERE JobTitle LIKE '%Developer%' OR JobTitle LIKE '%Engineer%';

--19. Retrieve a list of applicants and the jobs they have applied for, including those who have not applied and jobs without applicants.
SELECT a.FirstName, a.LastName, j.JobTitle
FROM Applicants a
CROSS JOIN Jobs j
LEFT JOIN Applications ap ON a.ApplicantID = ap.ApplicantID AND j.JobID = ap.JobID;

--20. List all combinations of applicants and companies where the company is in a specific city and the applicant has more than 2 years of experience. For example: city=Chennai
SELECT Applicants.FirstName, Applicants.LastName, Companies.CompanyName, Companies.Location
FROM Applicants
INNER JOIN Applications ON Applicants.ApplicantID = Applications.ApplicantID
INNER JOIN Jobs ON Applications.JobID = Jobs.JobID
INNER JOIN Companies ON Jobs.CompanyID = Companies.CompanyID
WHERE Applicants.Resume LIKE '%[3-9] years of experience%'
    OR Applicants.Resume LIKE '%[1-9][0-9]+ years of experience%' 
AND Companies.Location = 'Chennai';
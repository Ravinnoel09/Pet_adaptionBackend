-- Pet Table
CREATE TABLE Pet (
    pet_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    breed VARCHAR(50),
    age INT,
    status VARCHAR(20) CHECK (status IN ('Available', 'Adopted')),
    added_date DATE DEFAULT CURRENT_DATE
);

-- Owner Table
CREATE TABLE Owner (
    owner_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    address TEXT
);

-- Adoption Request Table
CREATE TABLE Adoption_Request (
    request_id SERIAL PRIMARY KEY,
    pet_id INT REFERENCES Pet(pet_id),
    owner_id INT REFERENCES Owner(owner_id),
    request_date DATE DEFAULT CURRENT_DATE,
    status VARCHAR(20) CHECK (status IN ('Pending', 'Approved', 'Rejected'))
);

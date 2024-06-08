import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [companies, setCompanies] = useState([]);
  const [name, setName] = useState('');
  const [industryCategory, setIndustryCategory] = useState('');
  const [industry, setIndustry] = useState('');
  const [city, setCity] = useState('');
  const [country, setCountry] = useState('');

  const fetchCompanies = () => {
    let url = '/api/companies/';
    const params = {};
    if (name) params.name = name;
    if (industryCategory) params.industry_category = industryCategory;
    if (industry) params.industry = industry;
    if (city) params.city = city;
    if (country) params.country = country;
    url += '?' + new URLSearchParams(params).toString();

    axios.get(url)
      .then(response => {
        console.log(response.data)
        setCompanies(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the companies!', error);
      });
  };

  useEffect(() => {
    fetchCompanies();
  }, []);

  const handleSubmit = (event) => {
    event.preventDefault();
    fetchCompanies();
  };

  return (
    <div className="container mt-4">
      <h1 className="mb-4">Company List</h1>

      <form onSubmit={handleSubmit} className="mb-4">
        <div className="form-group mr-2">
          <label htmlFor="name" className="mr-2">企業名</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="form-control"
          />
        </div>
        <div className="form-group mr-2">
          <label htmlFor="industryCategory" className="mr-2">業界大分類</label>
          <input
            type="text"
            id="industryCategory"
            value={industryCategory}
            onChange={(e) => setIndustryCategory(e.target.value)}
            className="form-control"
          />
        </div>
        <div className="form-group mr-2">
          <label htmlFor="industry" className="mr-2">業界中分類</label>
          <input
            type="text"
            id="industry"
            value={industry}
            onChange={(e) => setIndustry(e.target.value)}
            className="form-control"
          />
        </div>
        <div className="form-group mr-2">
          <label htmlFor="city" className="mr-2">市区町村</label>
          <input
            type="text"
            id="city"
            value={city}
            onChange={(e) => setCity(e.target.value)}
            className="form-control"
          />
        </div>
        <div className="form-group mr-2">
          <label htmlFor="country" className="mr-2">国</label>
          <input
            type="text"
            id="country"
            value={country}
            onChange={(e) => setCountry(e.target.value)}
            className="form-control"
          />
        </div>
        <button type="submit" className="btn btn-outline-success">Search</button>
      </form>

      <table className="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Company Name</th>
            <th scope="col">Industry</th>
            <th scope="col">Established Date</th>
            <th scope="col">Employees</th>
            <th scope="col">Revenue</th>
            <th scope="col">City</th>
            <th scope="col">Country</th>
          </tr>
        </thead>
        <tbody>
          {companies.map((company, index) => (
            <tr key={company.id}>
              <th scope="row">{index + 1}</th>
              <td>{company.name}</td>
              <td>{company.industry.name}</td>
              <td>{company.established_date}</td>
              <td>{company.employees}</td>
              <td>{company.revenue}</td>
              <td>{company.city}</td>
              <td>{company.country}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;

import React, { useState } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

const WeatherForm = ({ getWeather }) => {
  const [startDate, setStartDate] = useState("");
  const [startTime, setStartTime] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    const hour = startTime ? startTime.getHours() : "";
    getWeather(startDate, hour);
  };

  const minDate = new Date(2022, 8, 17, 5);
  const maxDate = new Date(2022, 9, 9, 4);
  return (
    <div style={{ display: "inline-flex" }} className="ui segment">
      <form onSubmit={handleSubmit} class="ui form">
        <h4 class="ui dividing header">Get Weather</h4>
        <div class="field">
          <div class="two fields">
            <div class="field">
              <label>Start Date</label>
              <DatePicker
                class="field"
                selected={startDate}
                onChange={(date) => setStartDate(date)}
                minDate={minDate}
                maxDate={maxDate}
                dateFormat="yyy/MM/dd"
                isClearable
              />
            </div>
            <div class="field">
              <label>Time</label>
              <DatePicker
                class="field"
                selected={startTime}
                onChange={(date) => setStartTime(date)}
                timeFormat="h aa"
                dateFormat="h aa"
                timeIntervals={60}
                showTimeSelect
                showTimeSelectOnly
                isClearable
              />
            </div>
          </div>
        </div>
        <button
          type="submit"
          style={{ marginTop: "10px" }}
          class="ui button"
          tabIndex="0"
        >
          Submit
        </button>
      </form>
    </div>
  );
};

export default WeatherForm;

import React, { useState } from "react";
import WeatherForm from "./WeatherForm";
import "react-datepicker/dist/react-datepicker.css";
const axios = require("axios");

const Weather = () => {
  const [content, setContent] = useState();
  const getWeatherContent = async (startDate, startTime) => {
    startDate = startDate ? startDate.toLocaleDateString("en-US") : "";
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/?start_date=${startDate}&start_time=${startTime}`
      );
      setContent(response.data);
    } catch (error) {
      setContent(error);
    }
  };

  const columns = [
    { name: "date_time_local", title: "Time", width: "two wide" },
    { name: "unixtime", title: "Unix Time", width: "one wide" },
    { name: "period_index", title: "Period Index", width: "one wide" },
    { name: "period_string", title: "Period String" },
    { name: "cloudprecip", title: "Cloud Precipitation" },
    { name: "visibility_other", title: "Visibility" },
    { name: "winds", title: "Winds" },
    { name: "temperatures", title: "Temperatures" },
    { name: "windchill", title: "Windchill" },
    { name: "humidex", title: "Humidity" },
    { name: "uv", title: "UV" },
  ];
  console.log("column.style");
  const tableHeaderColumns = columns.map((column) => {
    console.log(column.style);
    return <th class={column.width}>{column.title}</th>;
  });
  // const columns = [
  //   "date_time_local",
  //   "unixtime",
  //   "period_index",
  //   "period_string",
  //   "cloudprecip",
  //   "visibility_other",
  //   "winds",
  //   "temperatures",
  //   "windchill",
  //   "humidex",
  //   "uv",
  // ];

  // const tableHeader = (
  //   <thead>
  //     <tr>
  //       <th>date_time_local</th>
  //       <th>unixtime</th>
  //       <th>period_index</th>
  //       <th>period_string</th>
  //       <th>cloudprecip</th>
  //       <th>visibility_other</th>
  //       <th>winds</th>
  //       <th>temperatures</th>
  //       <th>windchill</th>
  //       <th>humidex</th>
  //       <th>uv</th>
  //     </tr>
  //   </thead>
  // );

  const tableHeader = (
    <thead>
      <tr>{tableHeaderColumns}</tr>
    </thead>
  );
  let table;
  if (!content) {
    table = <table class="ui celled striped table">{tableHeader}</table>;
  } else if (content instanceof Error) {
    table = (
      <React.Fragment>
        <table class="ui celled striped table">
          {tableHeader}
          <tbody></tbody>
        </table>
        <div>{`Received a ${content.message}`}</div>
      </React.Fragment>
    );
  } else {
    let items = content.map((item) => {
      return (
        <tr>
          {columns.map((column) => {
            return <td>{item[column.name]}</td>;
          })}
          {/* {Object.entries(item).map(([key, value], i) => {
            return <td>{value}</td>;
          })} */}
        </tr>
      );
    });
    table = (
      <table
        style={{ margin: "95%", margin: "auto" }}
        class="ui celled striped table"
      >
        {tableHeader}
        <tbody>{items}</tbody>
      </table>
    );
  }
  return (
    <div class="ui existing segment">
      <WeatherForm getWeather={getWeatherContent}></WeatherForm>
      {table}
    </div>
  );
};

export default Weather;

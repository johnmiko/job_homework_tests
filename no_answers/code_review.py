"""
Review this code
function getTableInfo(
  info,
  row,
  rowIndex,
  type,
  tableJson,
  apiColumns
) {
  const {
    fieldMapping,
    nestedResult = false,
    emptyValueMessage = "",
    isSpecialColumns = false,
  } = tableJson.data;
  const rowObject = { rowData: [] };

  fieldMapping.forEach((mapping) => {
    let { columns, isSingleField, columnName } = mapping;

    if (!isSpecialColumns) {
      columns = processTypeColumns(
        columns,
        row[0],
        isSpecialColumns
      );
    }

    const defaultColumnDetails = {};
    if (isSingleField) {
      const { index: mappingColumnIndex } = getColumnIndex(
        apiColumns,
        columnName
      );
      defaultColumnDetails.isSingleField = isSingleField;
      defaultColumnDetails.mappingColumnIndex = mappingColumnIndex;
    }

    columns.forEach((column, columnIndex) => {
      const columnDetails = {
        ...defaultColumnDetails,
        column,
        apiColumns,
        row,
        nestedResult,
        emptyValueMessage,
        columnIndex,
      };

      const columnText = getDataBasedOnResponse(columnDetails);
      const rowDetails = { column, columnText, rowNumber: rowIndex, row };
      let tempRow = generateRowObject(rowDetails);

      if (isSpecialColumns) {
        tempRow = getValueForRow(tempRow, row[0], columnIndex);
      }
      rowObject.rowData = rowObject.rowData.concat(tempRow);
    });
  });

  return rowObject;
}

"""

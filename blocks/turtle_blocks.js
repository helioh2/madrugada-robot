Blockly.Python['move_forward'] = function(block) {
  var value_distancia = Blockly.Python.valueToCode(block, 'distancia', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = 'turtle.forward('+value_distancia+')\n';
  return code;
};

Blockly.Python['move_backward'] = function(block) {
  var value_distancia = Blockly.Python.valueToCode(block, 'distancia', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = 'turtle.backward('+value_distancia+')\n';
  return code;
};

Blockly.Python['pen_up'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = 'turtle.pen_up()\n';
  return code;
};

Blockly.Python['pen_down'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = 'turtle.pen_down()\n';
  return code;
};

Blockly.Python['go_to'] = function(block) {
  var value_x = Blockly.Python.valueToCode(block, 'X', Blockly.Python.ORDER_ATOMIC);
  var value_y = Blockly.Python.valueToCode(block, 'Y', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = 'turtle.go_to('+value_x+', '+value_y+')\n';
  return code;
};

Blockly.Python['turn'] = function(block) {
  var dropdown_option = block.getFieldValue('option');
  var value_name = Blockly.Python.valueToCode(block, 'NAME', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code;
  if (dropdown_option == 'RIGHT') {
    code = 'turtle.turn_right('+value_name+')\n';
  } else {
    code = 'turtle.turn_left('+value_name+')\n';
  }
  return code;
};
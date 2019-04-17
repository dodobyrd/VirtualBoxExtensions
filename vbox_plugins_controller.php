<?php 

/**
 * vbox_plugins class
 *
 * @package munkireport
 * @author 
 **/
class vbox_plugins_controller extends Module_controller
{
	
	/*** Protect methods with auth! ****/
	function __construct()
	{
		// Store module path
		$this->module_path = dirname(__FILE__);
	}
	
  /**
 * Get vbox_plugins information for serial_number
 *
 * @param string $serial serial number
 **/
public function get_data($serial_number = '')
{
      $obj = new View();
      if( ! $this->authorized())
      {
          $obj->view('json', array('msg' => 'Not authorized'));
          return;
      }

      $vbox_plugins = new vbox_plugins_model($serial_number);
      $obj->view('json', array('msg' => $vbox_plugins->rs));
}

} // END class default_module

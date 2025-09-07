import * as React from 'react';
import ListSubheader from '@mui/material/ListSubheader';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Collapse from '@mui/material/Collapse';
import InboxIcon from '@mui/icons-material/MoveToInbox';
import SendIcon from '@mui/icons-material/Send';
import NotificationsIcon from '@mui/icons-material/Notifications';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import StarBorder from '@mui/icons-material/StarBorder';
import SpaceDashboardIcon from '@mui/icons-material/SpaceDashboard';
import DraftsIcon from '@mui/icons-material/Drafts';
import MovieIcon from '@mui/icons-material/Movie';
import PhotoIcon from '@mui/icons-material/Photo';
import VideocamIcon from '@mui/icons-material/Videocam';
import { Link, useLocation } from 'react-router';

export default function Menu() {
  const [open, setOpen] = React.useState(true);
  const location = useLocation()
  const path = location.pathname
  const handleClick = () => {
    setOpen(!open);
  };

  return (
    <List
      sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}
      component="nav"
      aria-labelledby="nested-list-subheader"
      subheader={
        <ListSubheader component="div" id="nested-list-subheader">
          User Information (Rename)
        </ListSubheader>
      }
    >
      <ListItemButton component={Link} to="/" selected={path=='/'}>
        <ListItemIcon>
          <SpaceDashboardIcon/>
        </ListItemIcon>
        <ListItemText primary="Dashboard" /> {/* add a dynamic counter maybe? */}
      </ListItemButton>
      <ListItemButton component={Link} to="/notifications" selected={path=='/notifications'}>
        <ListItemIcon>
          <NotificationsIcon/>
        </ListItemIcon>
        <ListItemText primary="Notifications"/>
      </ListItemButton>

      <ListItemButton onClick={handleClick}>
        <ListItemIcon>
          <MovieIcon/>
        </ListItemIcon>
        <ListItemText primary="Media" />
        {open ? <ExpandLess /> : <ExpandMore />}
      </ListItemButton>

      <Collapse in={open} timeout="auto" unmountOnExit>
        <List component="div" disablePadding>
          <ListItemButton sx={{ pl: 4 }} component = {Link} to="/pictures" selected={path == '/pictures'}>
            <ListItemIcon>
              <PhotoIcon/>
            </ListItemIcon>
            <ListItemText primary="Photos" />
          </ListItemButton>
          <ListItemButton sx={{ pl: 4 }} component = {Link} to="/videos" selected={path == '/videos'}>
            <ListItemIcon>
              <VideocamIcon/>
            </ListItemIcon>
            <ListItemText primary="Videos"/>
          </ListItemButton>
        </List>
      </Collapse>
    </List>
  );
}

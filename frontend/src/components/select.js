import React,{ useEffect} from "react";

import {Link} from 'react-router-dom';

import { makeStyles } from "@material-ui/core/styles";
import {Grid, Typography, Box, Hidden} from "@material-ui/core";
import Paper from '@material-ui/core/Paper';
import ButtonBase from '@material-ui/core/ButtonBase';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAddressBook,faPhone,faMailBulk } from '@fortawesome/free-solid-svg-icons'
import FacebookIcon from '@material-ui/icons/Facebook';
import InstagramIcon from '@material-ui/icons/Instagram';
import 'font-awesome/css/font-awesome.min.css';


import {useParams, useRouteMatch} from "react-router-dom";

const useStyles = makeStyles({
    root: {
        maxWidth: 345,
    },
});

function Select({
                         //state
                         shopDetail,
                         getProfileShop,
                     }){

    const classes = useStyles();

    return(

        <Box
            display="flex"
            justifyContent="center"
            alignItems="center"
            minHeight="90vh"
        >
            <Card className={classes.root} style={{width:'300px',marginRight:'10px'}}>
                <CardActionArea>
                    <h2 style={{marginLeft:'50px'}}>Launch Community</h2>
                </CardActionArea>
                <CardActions>
                    <Button size="small" style={{marginLeft:'80px'}} color="primary">
                        <Link to={'../dashboard'}>Get Started</Link>
                    </Button>
                </CardActions>
            </Card>
            <Card className={classes.root} style={{width:'300px',marginLeft:'10px'}}>
                <CardActionArea>
                    <h2 style={{marginLeft:'55px'}}>Launch Business</h2>
                </CardActionArea>
                <CardActions>
                    <Button size="small" style={{marginLeft:'80px'}} color="primary">
                        <Link to={'../dashboard'}>Get Stared</Link>
                    </Button>
                </CardActions>
            </Card>

        </Box>
    )
}



export default (Select);
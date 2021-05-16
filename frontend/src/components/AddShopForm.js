import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import {
  TextField,
  CssBaseline,
  Container,
  Grid,
  Button,
} from "@material-ui/core";

import { useFormik } from "formik";
import * as yup from "yup";

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  form: {
    width: "100%",
    marginTop: theme.spacing(1),
  },
  actionBtn: {
    margin: theme.spacing(3, 0, 2),
  },
}));

const validationSchema = yup.object({
  title: yup.string().required("Required!").min(1),
  address: yup.string().required().min(1),
});

export default function AddProductForm({ loading, onSave, onCancel }) {
  const classes = useStyles();

  const onSubmit = (values) => {
    onSave(values);
  };

  const formik = useFormik({
    initialValues: {
      title: "",
      email: "",
      latitude:"",
      longitude:"",
      discordId:"",
      discordUrl:"",
      fbUrl:"",
      instaUrl:"",
      address: "",
    },
    validationSchema,
    onSubmit,
  });

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <form className={classes.form} onSubmit={formik.handleSubmit}>
        <Grid container spacing={2}>
          <Grid item xs={12}>
            <TextField
              variant="outlined"
              fullWidth
              id="title"
              name="title"
              label="Title"
              value={formik.values.title}
              onChange={formik.handleChange}
              error={formik.touched.title && Boolean(formik.errors.title)}
              helperText={formik.touched.title && formik.errors.title}
            />
          </Grid>
          <Grid item xs={12}>
            <TextField
                variant="outlined"
                fullWidth
                rows={1}
                id="email"
                name="email"
                label="Email"
                value={formik.values.email}
                onChange={formik.handleChange}
                error={formik.touched.email && Boolean(formik.errors.email)}
                helperText={formik.touched.email && formik.errors.email}
            />
          </Grid>
          <Grid item xs={6}>
            <TextField
                variant="outlined"
                fullWidth
                rows={1}
                id="latitude"
                name="latitude"
                label="latitude"
                value={formik.values.latitude}
                onChange={formik.handleChange}
                error={formik.touched.latitude && Boolean(formik.errors.latitude)}
                helperText={formik.touched.latitude && formik.errors.latitude}
            />
          </Grid>
          <Grid item xs={6}>
            <TextField
                variant="outlined"
                fullWidth
                rows={1}
                id="longitude"
                name="longitude"
                label="longitude"
                value={formik.values.longitude}
                onChange={formik.handleChange}
                error={formik.touched.longitude && Boolean(formik.errors.longitude)}
                helperText={formik.touched.longitude && formik.errors.longitude}
            />
          </Grid>
          <Grid item xs={6}>
            <TextField
                variant="outlined"
                fullWidth
                rows={1}
                id="discordId"
                name="discordId"
                label="discordId"
                value={formik.values.discordId}
                onChange={formik.handleChange}
                error={formik.touched.discordId && Boolean(formik.errors.discordId)}
                helperText={formik.touched.email && formik.errors.email}
            />
          </Grid>
          <Grid item xs={6}>
            <TextField
                variant="outlined"
                fullWidth
                rows={1}
                id="discordUrl"
                name="discordUrl"
                label="discordUrl"
                value={formik.values.discordUrl}
                onChange={formik.handleChange}
                error={formik.touched.discordUrl && Boolean(formik.errors.discordUrl)}
                helperText={formik.touched.discordUrl && formik.errors.discordUrl}
            />
          </Grid>
          <Grid item xs={12}>
            <TextField
              variant="outlined"
              multiline
              fullWidth
              rows={8}
              id="address"
              name="address"
              label="address"
              value={formik.values.address}
              onChange={formik.handleChange}
              error={formik.touched.address && Boolean(formik.errors.address)}
              helperText={formik.touched.address && formik.errors.address}
            />
          </Grid>

          <Grid item xs={4}>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.actionBtn}
              disabled={loading}
            >
              Save
            </Button>
          </Grid>

          <Grid item xs={4}>
            <Button
              fullWidth
              color="primary"
              className={classes.actionBtn}
              onClick={onCancel}
              disabled={loading}
            >
              Cancel
            </Button>
          </Grid>
        </Grid>
      </form>
    </Container>
  );
}

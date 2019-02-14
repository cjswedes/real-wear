Features/UserStories/Tasks

* Basically just how we have to get started.

System Task:
	Details: Create python web app that can run locally with a basic home page
	* Use this for all development
	* Do we assume that all users are using Chrome?
	* See UserStory1 for more details
	
* This can be a large part of the proposal specifications.  There is a lot here that can be discussed and decided on to create our specification.

UserStory1:
    * Iteration 1
	User Action: Be able too see a Home page with About, Shop By Department, Customer Profiles, and Documents tab
	
	System Requirements:
		* Have backend service to serve correct page given different URL routes (one for each tab)
		* Have database to store and retrieve the data for each page (where the back-end service will get the data from)
		* Front-end should be able to display arbitrary lists of the data (data needs vary depending on the tab)
	
	Tasks:
		1. Decide on the database storage system: postgresql works decently, there are many options here
		2. Make final decision on what backend packages we will build the app on (i.e django, flask, etc.)
		3. Make html templates for the frontend (Not sure if this is needed, since I dont know what the frontend technology will be). Basically do the front end part, whatever that entails.
		4. Create endpoints for each URL route (each tab)
		5. Create service methods for each URL route to harness to gather the correct data from the database
		6. Create css theme for the HTML (possible copy this from some other UW site)
		7. Gather Graphics/ other theme related points from current website and the user
		8. Document everything as you go!

*We can put down our own requirements for this, but I think we need to run it by the user to ensure they agree with what we think is an improvement in accessibility.		

UserStory2:
	* Iteration 1 and/or 2
	
	User Action: Improve the accessibility of the Customer profiles page. Be able to view useful information about how that customer compares to the other customers in the database
	
	System Requirements:
		* Need to Define based on more specific requirements
	
	Tasks:
	
UserStory3:
    * Iteration 2
	
	User Action: An admin of the website can upload additional data (of the same format) to the database. They can delete data files from the database, they can update current data files from the database. Ask User if this needs to be done through the website itself (harder) or can simply be done by modifying source files, and redeloying the website (easier).
	
	System Requirements (Assumes the easier option):
		* Define deployment process
		* Document protocol for updating, adding, and deleteing source data files.
	
	Tasks:
		1. Determine and then document the deployment process. This should be an easy task for the user to perform. Probably need to discuss with them to see what they are capable of, or are doing right now.
		2. Document the steps so any user can do it!
		
UserStory4:
	* Iteration 2
	* This really needs discussion to decide what this visualization will be. In my opinion, I think we should start with just some graphs that show conclusions from the dataset. However, the visualizations could also be something like a model of what certain outfits look like (i.e. putting clothes on a model of some sort that the user can view and interact with). This model idea is outlined more in UserStory 5.1 and 5.2.
	
	User Action: User can navigate to a "Discover" page where they will be able to see various visual representations of the data as a whole.  The goal of this needs help from the User to define. They need to answer the question: "What do you want the viewers to understand about the datasets?". Only they can answer this question since they are the ones who have been studying the data.
	
	System Requirements:
		* have a backend service/function to perform the data analysis and create each visualization the user wants (possibly incorporate inputs from the user)
		* They should be displayed in a clear, concise format that fits with the rest of the website's theme
	
	Tasks:
		1. Create each backend service for each visualization
		2. Do the frontend stuff, this is reallly important in ensuring the visuallizations are meaningful/interesting

*This is a general cleaning up task that will surely get longer as we go through the project and forget to document some things. Not critical to proposal.		

System Task:
	* Do all the dumb documentation that we didn't do so that we get a good grade
	* Make sure we are on track with the class requirements and ready to demo existing functionality

* This story (5.1 and 5.2) could be done if we want to tackle it, but it will for sure take two iterations. We need to decide if we want to go this route, the route of making other visualizations, doing both, or just something else entirely. I think it is worth telling the user about this option to see if its something they would really want. Make sure they understand that if they want this, they might not get too many other features.

UserStory5.1:
	UserAction: user uploads a photo to the site (the photo is used once just for that session, so we dont have to handle logins/authentication). They are then shown a 3D representation of their face attached to a standard body which will allow them to rotate.
	
	System Requirements:
		* Backend service that takes in 2d photo and outputs the 3d face
		* backend service that stitches that face to a sttandard 3d body (possible enhancements of giving the user some control over the body shape/size)
		* Front end display of the 3D model that the user can then interact with by rotating
		* Be sure to think about how clothes images might be added to the body
	
	Tasks:
		1. Define the backend service for making 3d face, gather the right code from researchers and put into our backend
		2. Define the backend service that takes in body input and 3d face and then stitches them together. 
		3. find a frontend module that will work to view the 3D model in the browser
	
UserStory5.2:
	
	UserAction:	User can update the 3D model by adding shirt/pants, or dress, etc. to the 3d model
	
	System Requirements:
		* Need the data structures for the clothes
		* need to be able to update the 3d model to have different "skin"
		* need to be able to easily select what clothes to put on the user.
	
	Tasks:
		1. define how the clothes can be added to the 3D model
		2. Create backend service to add one arbitrary piece of clothes to an arbitrary model
		3. Create the frontend components for selecting which pieces of clothing are to be put on the model.
		
*This is something a few of us could implement in one iteration. But we need to talk to the user to see if this is something that she thinks would be useful to increase interactiveness with the website.

UserStory6:
	* Iteration 3.
	
	UserAction: There is a blog feed that the admin user can update by posting new posts, editing old posts, or deleting posts. They can add media to the blog posts as well (pictures/video/links)
	
	System Requirements:
		* all blog posts can be managed by the administrator
		* there needs to be some way to identify administrator, (maybe there is a page where blog posters can login)
		* Have database table to store all the blog posts (Data needs to persist between deployments)
		* Blog is displayed along the themes of the rest of the website
		* possible enhancement: allow people to comment (could be a whole other user story)
	
	Tasks:
		1. Design architecture for defining an administrator users on the website
		2. Create backend service to serve the available blog posts for the general user
		3. create backend services for adding, deleting, and updating the blog posts. It should only be accessible by admins
		4. Create frontend templates for viewing the blog as a regular user
		5. Create frontend templates for maintaining the blog as an admin user
		

		
		



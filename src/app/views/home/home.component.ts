import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Location } from '@angular/common';
import { IgxCarouselComponent } from 'igniteui-angular';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor(public router: Router, private location: Location) { }

  @ViewChild('carousel', { static: true }) public carousel: IgxCarouselComponent;

  public slides: any[] = [];
  public animations = ['slide', 'fade', 'none'];

  public ngOnInit() {
    this.addSlides();
  }

  public addSlides() {
    this.slides.push(
      {
        description: '30+ Material-based Angular components to code speedy web apps faster.',
        heading: 'Ignite UI for Angular',
        image: 'https://www.infragistics.com/angular-demos/assets/images/carousel/slide1-angular.png',
        link: 'https://www.infragistics.com/products/ignite-ui-angular'
      },
      {
        description: 'A complete JavaScript UI library empowering you to build data-rich responsive web apps.',
        heading: 'Ignite UI for Javascript',
        image: 'https://www.infragistics.com/angular-demos/assets/images/carousel/slide2-ignite.png',
        link: 'https://www.infragistics.com/products/ignite-ui'
      },
      {
        description: 'Build full-featured business apps with the most versatile set of ASP.NET AJAX UI controls',
        heading: 'Ultimate UI for ASP.NET',
        image: 'https://www.infragistics.com/angular-demos/assets/images/carousel/slide3-aspnet.png',
        link: 'https://www.infragistics.com/products/aspnet'
      }
    );
  }

  public goTo() {
    this.router.navigate(['tarifarito']);
  }

  goBack(): void {
    this.location.back();
  }

}
